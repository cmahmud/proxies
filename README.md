# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 346
- HTTP: 133 alive / 40 gold
- HTTPS: 57 alive / 9 gold
- SOCKS4: 167 alive / 154 gold
- SOCKS5: 198 alive / 143 gold

## Historical pool

- Discovered: 171565
- Ever alive: 32882
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
