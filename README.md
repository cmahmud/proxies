# SyndProxy private pool

## Current pool

- Alive now: 1028
- Gold now: 507
- HTTP: 359 alive / 147 gold
- HTTPS: 262 alive / 87 gold
- SOCKS4: 187 alive / 117 gold
- SOCKS5: 220 alive / 156 gold

## Historical pool

- Discovered: 118125
- Ever alive: 17786
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
