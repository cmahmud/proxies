# SyndProxy private pool

## Current pool

- Alive now: 735
- Gold now: 386
- HTTP: 197 alive / 76 gold
- HTTPS: 116 alive / 22 gold
- SOCKS4: 221 alive / 143 gold
- SOCKS5: 201 alive / 145 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25243
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
