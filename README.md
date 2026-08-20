# SyndProxy private pool

## Current pool

- Alive now: 1769
- Gold now: 647
- HTTP: 689 alive / 217 gold
- HTTPS: 556 alive / 117 gold
- SOCKS4: 223 alive / 149 gold
- SOCKS5: 301 alive / 164 gold

## Historical pool

- Discovered: 142688
- Ever alive: 24268
- Ever gold: 971

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
