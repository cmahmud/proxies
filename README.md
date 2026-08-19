# SyndProxy private pool

## Current pool

- Alive now: 1002
- Gold now: 533
- HTTP: 331 alive / 160 gold
- HTTPS: 242 alive / 89 gold
- SOCKS4: 226 alive / 152 gold
- SOCKS5: 203 alive / 132 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18081
- Ever gold: 715

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
