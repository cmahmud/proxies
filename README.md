# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 464
- HTTP: 128 alive / 96 gold
- HTTPS: 49 alive / 32 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 187 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49410
- Ever gold: 1580

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
