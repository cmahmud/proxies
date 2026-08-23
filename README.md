# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 346
- HTTP: 121 alive / 41 gold
- HTTPS: 42 alive / 9 gold
- SOCKS4: 172 alive / 153 gold
- SOCKS5: 188 alive / 143 gold

## Historical pool

- Discovered: 171565
- Ever alive: 32887
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
