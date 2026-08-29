# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 440
- HTTP: 126 alive / 88 gold
- HTTPS: 62 alive / 26 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43662
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
