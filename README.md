# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 440
- HTTP: 128 alive / 84 gold
- HTTPS: 122 alive / 23 gold
- SOCKS4: 165 alive / 162 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34328
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
