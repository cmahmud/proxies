# SyndProxy validated proxy pool

## Current pool

- Alive now: 892
- Gold now: 16
- HTTP: 456 alive / 12 gold
- HTTPS: 123 alive / 1 gold
- SOCKS4: 144 alive / 0 gold
- SOCKS5: 169 alive / 3 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32662
- Ever gold: 1192

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
