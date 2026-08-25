# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 420
- HTTP: 81 alive / 62 gold
- HTTPS: 79 alive / 20 gold
- SOCKS4: 172 alive / 164 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36188
- Ever gold: 1269

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
