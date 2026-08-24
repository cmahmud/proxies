# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 444
- HTTP: 128 alive / 86 gold
- HTTPS: 94 alive / 24 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 197 alive / 173 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34404
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
