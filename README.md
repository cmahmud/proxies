# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 460
- HTTP: 131 alive / 91 gold
- HTTPS: 129 alive / 32 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 221 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46060
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
