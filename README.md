# SyndProxy private pool

## Current pool

- Alive now: 898
- Gold now: 392
- HTTP: 282 alive / 77 gold
- HTTPS: 164 alive / 22 gold
- SOCKS4: 216 alive / 149 gold
- SOCKS5: 236 alive / 144 gold

## Historical pool

- Discovered: 165846
- Ever alive: 32377
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
