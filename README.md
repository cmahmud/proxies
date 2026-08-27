# SyndProxy validated proxy pool

## Current pool

- Alive now: 658
- Gold now: 409
- HTTP: 122 alive / 67 gold
- HTTPS: 162 alive / 13 gold
- SOCKS4: 183 alive / 159 gold
- SOCKS5: 191 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40851
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
