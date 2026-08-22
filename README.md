# SyndProxy private pool

## Current pool

- Alive now: 879
- Gold now: 435
- HTTP: 233 alive / 93 gold
- HTTPS: 153 alive / 30 gold
- SOCKS4: 229 alive / 152 gold
- SOCKS5: 264 alive / 160 gold

## Historical pool

- Discovered: 163285
- Ever alive: 31816
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
