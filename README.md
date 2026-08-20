# SyndProxy private pool

## Current pool

- Alive now: 766
- Gold now: 372
- HTTP: 221 alive / 69 gold
- HTTPS: 129 alive / 18 gold
- SOCKS4: 222 alive / 143 gold
- SOCKS5: 194 alive / 142 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25495
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
