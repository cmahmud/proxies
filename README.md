# SyndProxy private pool

## Current pool

- Alive now: 1188
- Gold now: 444
- HTTP: 394 alive / 103 gold
- HTTPS: 262 alive / 29 gold
- SOCKS4: 257 alive / 153 gold
- SOCKS5: 275 alive / 159 gold

## Historical pool

- Discovered: 159282
- Ever alive: 30440
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
