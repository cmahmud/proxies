# SyndProxy private pool

## Current pool

- Alive now: 1177
- Gold now: 425
- HTTP: 373 alive / 96 gold
- HTTPS: 314 alive / 28 gold
- SOCKS4: 222 alive / 147 gold
- SOCKS5: 268 alive / 154 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28234
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
