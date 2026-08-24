# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 442
- HTTP: 126 alive / 86 gold
- HTTPS: 91 alive / 22 gold
- SOCKS4: 166 alive / 162 gold
- SOCKS5: 184 alive / 172 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34298
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
