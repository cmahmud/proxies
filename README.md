# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 431
- HTTP: 93 alive / 71 gold
- HTTPS: 123 alive / 33 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47307
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
