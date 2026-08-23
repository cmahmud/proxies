# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 345
- HTTP: 122 alive / 39 gold
- HTTPS: 41 alive / 9 gold
- SOCKS4: 164 alive / 153 gold
- SOCKS5: 188 alive / 144 gold

## Historical pool

- Discovered: 171565
- Ever alive: 32885
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
