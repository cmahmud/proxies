# SyndProxy private pool

## Current pool

- Alive now: 743
- Gold now: 354
- HTTP: 196 alive / 67 gold
- HTTPS: 127 alive / 18 gold
- SOCKS4: 221 alive / 144 gold
- SOCKS5: 199 alive / 125 gold

## Historical pool

- Discovered: 145548
- Ever alive: 25398
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
