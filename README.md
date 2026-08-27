# SyndProxy validated proxy pool

## Current pool

- Alive now: 675
- Gold now: 409
- HTTP: 129 alive / 62 gold
- HTTPS: 181 alive / 12 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 188 alive / 175 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40819
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
