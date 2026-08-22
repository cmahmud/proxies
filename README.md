# SyndProxy private pool

## Current pool

- Alive now: 749
- Gold now: 414
- HTTP: 188 alive / 88 gold
- HTTPS: 130 alive / 28 gold
- SOCKS4: 201 alive / 140 gold
- SOCKS5: 230 alive / 158 gold

## Historical pool

- Discovered: 163856
- Ever alive: 31959
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
