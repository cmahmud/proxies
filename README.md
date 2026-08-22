# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 437
- HTTP: 326 alive / 95 gold
- HTTPS: 229 alive / 32 gold
- SOCKS4: 211 alive / 141 gold
- SOCKS5: 274 alive / 169 gold

## Historical pool

- Discovered: 161986
- Ever alive: 31266
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
