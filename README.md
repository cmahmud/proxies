# SyndProxy private pool

## Current pool

- Alive now: 700
- Gold now: 392
- HTTP: 171 alive / 83 gold
- HTTPS: 117 alive / 21 gold
- SOCKS4: 211 alive / 143 gold
- SOCKS5: 201 alive / 145 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25222
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
