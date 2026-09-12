# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 452
- HTTP: 131 alive / 95 gold
- HTTPS: 55 alive / 31 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49326
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
