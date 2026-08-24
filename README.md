# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 386
- HTTP: 111 alive / 67 gold
- HTTPS: 49 alive / 14 gold
- SOCKS4: 164 alive / 153 gold
- SOCKS5: 176 alive / 152 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33248
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
