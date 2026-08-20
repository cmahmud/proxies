# SyndProxy private pool

## Current pool

- Alive now: 766
- Gold now: 386
- HTTP: 190 alive / 78 gold
- HTTPS: 141 alive / 16 gold
- SOCKS4: 214 alive / 147 gold
- SOCKS5: 221 alive / 145 gold

## Historical pool

- Discovered: 148343
- Ever alive: 26409
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
