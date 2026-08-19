# SyndProxy private pool

## Current pool

- Alive now: 1035
- Gold now: 530
- HTTP: 335 alive / 159 gold
- HTTPS: 269 alive / 88 gold
- SOCKS4: 229 alive / 152 gold
- SOCKS5: 202 alive / 131 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18121
- Ever gold: 715

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
