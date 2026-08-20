# SyndProxy private pool

## Current pool

- Alive now: 740
- Gold now: 358
- HTTP: 193 alive / 76 gold
- HTTPS: 159 alive / 22 gold
- SOCKS4: 212 alive / 143 gold
- SOCKS5: 176 alive / 117 gold

## Historical pool

- Discovered: 145543
- Ever alive: 25344
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
