# SyndProxy private pool

## Current pool

- Alive now: 971
- Gold now: 359
- HTTP: 312 alive / 77 gold
- HTTPS: 206 alive / 18 gold
- SOCKS4: 203 alive / 127 gold
- SOCKS5: 250 alive / 137 gold

## Historical pool

- Discovered: 158224
- Ever alive: 29848
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
