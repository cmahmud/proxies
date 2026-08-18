# SyndProxy private pool

## Current pool

- Alive now: 842
- Gold now: 280
- HTTP: 282 alive / 40 gold
- HTTPS: 168 alive / 8 gold
- SOCKS4: 219 alive / 140 gold
- SOCKS5: 173 alive / 92 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13798
- Ever gold: 430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
