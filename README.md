# SyndProxy private pool

## Current pool

- Alive now: 819
- Gold now: 382
- HTTP: 237 alive / 88 gold
- HTTPS: 164 alive / 25 gold
- SOCKS4: 200 alive / 123 gold
- SOCKS5: 218 alive / 146 gold

## Historical pool

- Discovered: 163880
- Ever alive: 32033
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
