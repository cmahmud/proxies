# SyndProxy private pool

## Current pool

- Alive now: 1238
- Gold now: 402
- HTTP: 407 alive / 92 gold
- HTTPS: 315 alive / 20 gold
- SOCKS4: 232 alive / 138 gold
- SOCKS5: 284 alive / 152 gold

## Historical pool

- Discovered: 134569
- Ever alive: 22183
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
