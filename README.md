# SyndProxy private pool

## Current pool

- Alive now: 929
- Gold now: 469
- HTTP: 300 alive / 115 gold
- HTTPS: 197 alive / 88 gold
- SOCKS4: 211 alive / 125 gold
- SOCKS5: 221 alive / 141 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17494
- Ever gold: 666

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
