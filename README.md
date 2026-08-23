# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 364
- HTTP: 105 alive / 38 gold
- HTTPS: 46 alive / 10 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 194 alive / 158 gold

## Historical pool

- Discovered: 171593
- Ever alive: 32934
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
