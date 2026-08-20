# SyndProxy private pool

## Current pool

- Alive now: 659
- Gold now: 382
- HTTP: 168 alive / 62 gold
- HTTPS: 85 alive / 16 gold
- SOCKS4: 202 alive / 151 gold
- SOCKS5: 204 alive / 153 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25726
- Ever gold: 1073

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
