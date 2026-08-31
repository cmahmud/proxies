# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 462
- HTTP: 131 alive / 93 gold
- HTTPS: 128 alive / 32 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 222 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46060
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
