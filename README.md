# SyndProxy private pool

## Current pool

- Alive now: 838
- Gold now: 384
- HTTP: 251 alive / 72 gold
- HTTPS: 173 alive / 16 gold
- SOCKS4: 207 alive / 148 gold
- SOCKS5: 207 alive / 148 gold

## Historical pool

- Discovered: 148583
- Ever alive: 26469
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
