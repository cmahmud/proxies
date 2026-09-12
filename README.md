# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 420
- HTTP: 103 alive / 76 gold
- HTTPS: 49 alive / 22 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 175 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49452
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
