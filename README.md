# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 440
- HTTP: 114 alive / 77 gold
- HTTPS: 92 alive / 33 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 181 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47014
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
