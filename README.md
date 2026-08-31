# SyndProxy validated proxy pool

## Current pool

- Alive now: 680
- Gold now: 464
- HTTP: 144 alive / 96 gold
- HTTPS: 129 alive / 30 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 235 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46258
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
