# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 460
- HTTP: 131 alive / 92 gold
- HTTPS: 53 alive / 33 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49404
- Ever gold: 1580

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
