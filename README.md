# SyndProxy private pool

## Current pool

- Alive now: 1681
- Gold now: 609
- HTTP: 728 alive / 201 gold
- HTTPS: 550 alive / 143 gold
- SOCKS4: 176 alive / 101 gold
- SOCKS5: 227 alive / 164 gold

## Historical pool

- Discovered: 143425
- Ever alive: 24695
- Ever gold: 1032

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
