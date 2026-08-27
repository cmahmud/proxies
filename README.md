# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 420
- HTTP: 105 alive / 69 gold
- HTTPS: 143 alive / 24 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41298
- Ever gold: 1324

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
