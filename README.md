# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 456
- HTTP: 127 alive / 84 gold
- HTTPS: 129 alive / 32 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 194 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46749
- Ever gold: 1449

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
