# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 359
- HTTP: 84 alive / 33 gold
- HTTPS: 44 alive / 10 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 178 alive / 161 gold

## Historical pool

- Discovered: 171600
- Ever alive: 32943
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
