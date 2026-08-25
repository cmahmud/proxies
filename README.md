# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 419
- HTTP: 94 alive / 64 gold
- HTTPS: 81 alive / 21 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 194 alive / 171 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36118
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
