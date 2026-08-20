# SyndProxy private pool

## Current pool

- Alive now: 800
- Gold now: 392
- HTTP: 213 alive / 81 gold
- HTTPS: 157 alive / 18 gold
- SOCKS4: 209 alive / 147 gold
- SOCKS5: 221 alive / 146 gold

## Historical pool

- Discovered: 148343
- Ever alive: 26412
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
