# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 384
- HTTP: 123 alive / 66 gold
- HTTPS: 49 alive / 15 gold
- SOCKS4: 172 alive / 151 gold
- SOCKS5: 186 alive / 152 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33224
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
