# SyndProxy private pool

## Current pool

- Alive now: 1831
- Gold now: 644
- HTTP: 719 alive / 218 gold
- HTTPS: 596 alive / 116 gold
- SOCKS4: 223 alive / 148 gold
- SOCKS5: 293 alive / 162 gold

## Historical pool

- Discovered: 142688
- Ever alive: 24272
- Ever gold: 971

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
