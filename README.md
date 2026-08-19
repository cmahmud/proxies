# SyndProxy private pool

## Current pool

- Alive now: 1345
- Gold now: 389
- HTTP: 485 alive / 94 gold
- HTTPS: 315 alive / 21 gold
- SOCKS4: 237 alive / 131 gold
- SOCKS5: 308 alive / 143 gold

## Historical pool

- Discovered: 134553
- Ever alive: 22115
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
