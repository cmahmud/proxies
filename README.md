# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 427
- HTTP: 144 alive / 78 gold
- HTTPS: 89 alive / 23 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 194 alive / 164 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33896
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
